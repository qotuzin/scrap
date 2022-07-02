#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine.h"
using namespace std;

#include <fstream>
#include <strstream>

struct vec3d
{
	float x, y, z;
};

struct mat4x4
{
	float m[4][4] = { 0 };
};

struct triangle
{
	vec3d p[3];

	int colour[3];
};

struct mesh
{
	vector<triangle> tris;

	bool LoadFromObjectFile(string sFilename)
	{
		ifstream f(sFilename);
		if (!f.is_open())
			cout << "file could not load." << endl;
			return false;

			// Local cache of verts
			vector<vec3d> verts;

			while(!f.eof())	
			{
				char line[128];
				f.getline(line, 128);

				strstream s;
				s << line;

				char junk;

				if (line[0] == 'v')
				{
					vec3d v;
					s >> junk >> v.x >> v.y >> v.z;
					verts.push_back(v);

				if (line[0] == 'f')
				{	
					string f_raw[4];
					int f[4];
					s >> junk >> f_raw[0] >> f_raw[1] >> f_raw[2] >> f_raw[3];
					cout << f_raw[0] << endl;

					for (int n = 0; n < 4; n++)
					{
						if (f_raw[n][1] == '/')
							f_raw[n].erase(1);
						else if (f_raw[0][2] == '/')
							f_raw[n].erase(2);
						else if (f_raw[0][3] == '/')
							f_raw[n].erase(3);
						
						f[n] = stoi(f_raw[n]);
					
					}

					tris.push_back({ verts[f[0] - 1], verts[f[1] - 1], verts[f[2 - 1]] });
					tris.push_back({ verts[f[0] - 1], verts[f[2] - 1], verts[f[3 - 1]] });
				}
				}
			}
		return true;
	}
};

class olcEngine3D : public olc::PixelGameEngine
{
public: 
	olcEngine3D()
	{
		sAppName = "OLC 3D Game Engine";
	}

private:
	mesh meshCube;
	mesh meshImport;
	mat4x4 matProj;

	vec3d vCamera;

	float fTheta;

	void MultiplyMatrixVector(vec3d &i, vec3d &o, mat4x4 &m)
	{
		o.x = i.x * m.m[0][0] + i.y * m.m[1][0] + i.z * m.m[2][0] + m.m[3][0];
		o.y = i.x * m.m[0][1] + i.y * m.m[1][1] + i.z * m.m[2][1] + m.m[3][1];
		o.z = i.x * m.m[0][2] + i.y * m.m[1][2] + i.z * m.m[2][2] + m.m[3][2];
		float w = i.x * m.m[0][3] + i.y * m.m[1][3] + i.z * m.m[2][3] + m.m[3][3];

		if (w != 0)
		{
			o.x /= w; o.y /= w; o.z /= w;
		}
		
	}
	
public:	
	bool OnUserCreate() override
	{ //Called once at start
		meshImport.LoadFromObjectFile("pizzaBox.obj");

		meshCube.tris = {

			// SOUTH
			{ 0.0f, 0.0f, 0.0f,    0.0f, 1.0f, 0.0f,    1.0f, 1.0f, 0.0f },
			{ 0.0f, 0.0f, 0.0f,    1.0f, 1.0f, 0.0f,    1.0f, 0.0f, 0.0f },
			
			// EAST
			{ 1.0f, 0.0f, 0.0f,    1.0f, 1.0f, 0.0f,    1.0f, 1.0f, 1.0f },
			{ 1.0f, 0.0f, 0.0f,    1.0f, 1.0f, 1.0f,    1.0f, 0.0f, 1.0f },

			// NORTH
			{ 1.0f, 0.0f, 1.0f,    1.0f, 1.0f, 1.0f,    0.0f, 1.0f, 1.0f },
			{ 1.0f, 0.0f, 1.0f,    0.0f, 1.0f, 1.0f,    0.0f, 0.0f, 1.0f },

			// WEST
			{ 0.0f, 0.0f, 1.0f,    0.0f, 1.0f, 1.0f,    0.0f, 1.0f, 0.0f },
			{ 0.0f, 0.0f, 1.0f,    0.0f, 1.0f, 0.0f,    0.0f, 0.0f, 0.0f },

			// TOP
			{ 0.0f, 1.0f, 0.0f,    0.0f, 1.0f, 1.0f,    1.0f, 1.0f, 1.0f },
			{ 0.0f, 1.0f, 0.0f,    1.0f, 1.0f, 1.0f,    1.0f, 1.0f, 0.0f },

			// BOTTOM
			{ 1.0f, 0.0f, 1.0f,    0.0f, 0.0f, 1.0f,    0.0f, 0.0f, 0.0f },
			{ 1.0f, 0.0f, 1.0f,    0.0f, 0.0f, 0.0f,    1.0f, 0.0f, 0.0f },

		};

		// Projection Matrix

		float fNear = 0.1f;
		float fFar = 1000.0f;
		float fFov = 90.0f;
		float fAspectRatio = (float)ScreenHeight() / (float)ScreenWidth();
		float fFovRad = 1.0f / tan(fFov * 0.5f / 180.0f * 3.14159f);

		matProj.m[0][0] = fAspectRatio * fFovRad;
		matProj.m[1][1] = fFovRad;
		matProj.m[2][2] = fFar / (fFar - fNear);
		matProj.m[3][2] = (-fFar * fNear) / (fFar - fNear);
		matProj.m[2][3] = 1.0f;
		//matProj.m[3][3]	= 0.0f;
	
	
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{ //Called once every frame

		Clear(olc::BLACK);

		mat4x4 matRotZ, matRotX;
		fTheta += 1.0f * fElapsedTime;

		// Rotation Z
		matRotZ.m[0][0] = cosf(fTheta);
		matRotZ.m[0][1] = sinf(fTheta);
		matRotZ.m[1][0] = -sinf(fTheta);
		matRotZ.m[1][1] = cosf(fTheta);
		matRotZ.m[2][2] = 1;
		matRotZ.m[3][3] = 1;

		// Rotation X
		matRotX.m[0][0] = 1;
		matRotX.m[1][1] = cosf(fTheta * 0.5f);
		matRotX.m[1][2] = sinf(fTheta * 0.5f);
		matRotX.m[2][1] = -sinf(fTheta * 0.5f);
		matRotX.m[2][2] = cosf(fTheta * 0.5f);
		matRotX.m[3][3] = 1;



		// Draw Triangles

		for(auto tri : meshImport.tris)
		{
			triangle triProjected, triTranslated, triRotatedZ, triRotatedX;

			// Rotate in Z-Axis
			MultiplyMatrixVector(tri.p[0], triRotatedZ.p[0], matRotZ);
			MultiplyMatrixVector(tri.p[1], triRotatedZ.p[1], matRotZ);
			MultiplyMatrixVector(tri.p[2], triRotatedZ.p[2], matRotZ);

			// Rotate in X-Axis
			MultiplyMatrixVector(triRotatedZ.p[0], triRotatedX.p[0], matRotX);
			MultiplyMatrixVector(triRotatedZ.p[1], triRotatedX.p[1], matRotX);
			MultiplyMatrixVector(triRotatedZ.p[2], triRotatedX.p[2], matRotX);

			triTranslated = triRotatedX;
			triTranslated.p[0].z = triRotatedX.p[0].z + 3.0f;
			triTranslated.p[1].z = triRotatedX.p[1].z + 3.0f;
			triTranslated.p[2].z = triRotatedX.p[2].z + 3.0f;
			

			vec3d normal, line1, line2;
			line1.x = triTranslated.p[1].x - triTranslated.p[0].x;
			line1.y = triTranslated.p[1].y - triTranslated.p[0].y;
			line1.z = triTranslated.p[1].z - triTranslated.p[0].z;
			
			line2.x = triTranslated.p[2].x - triTranslated.p[0].x;
			line2.y = triTranslated.p[2].y - triTranslated.p[0].y;
			line2.z = triTranslated.p[2].z - triTranslated.p[0].z;

			normal.x = line1.y * line2.z - line1.z * line2.y;
			normal.y = line1.z * line2.x - line1.x * line2.z;
			normal.z = line1.x * line2.y - line1.y * line2.x;

			float l = sqrtf(normal.x * normal.x + normal.y * normal.y + normal.z * normal.z);
			normal.x /= l; normal.y /= l; normal.z /= l;


			if (normal.x * (triTranslated.p[0].x - vCamera.x) +
				normal.y * (triTranslated.p[0].y - vCamera.y) +
				normal.z * (triTranslated.p[0].z - vCamera.z) < 0.0f)

			{
				// Illumination
				vec3d light_direction = { 0.0f, 0.0f, -1.0f };
				float l = sqrtf(normal.x * normal.x + normal.y * normal.y + normal.z * normal.z);
				light_direction.x /= l; light_direction.y /= l; light_direction.z /= l;

				float light_dp = normal.x * light_direction.x + normal.y * light_direction.y + normal.z * light_direction.z;

				triTranslated.colour[0] = light_dp * 255;
				triTranslated.colour[1] = light_dp * 255;
				triTranslated.colour[2] = light_dp * 255;
				
				
				MultiplyMatrixVector(triTranslated.p[0], triProjected.p[0], matProj);
				MultiplyMatrixVector(triTranslated.p[1], triProjected.p[1], matProj);
				MultiplyMatrixVector(triTranslated.p[2], triProjected.p[2], matProj);
				
				triProjected.colour[0] = triTranslated.colour[0];
				triProjected.colour[1] = triTranslated.colour[1];
				triProjected.colour[2] = triTranslated.colour[2];

				
				// Scale into view
				triProjected.p[0].x += 1.0f; triProjected.p[0].y += 1.0f;
				triProjected.p[1].x += 1.0f; triProjected.p[1].y += 1.0f;
				triProjected.p[2].x += 1.0f; triProjected.p[2].y += 1.0f;

				triProjected.p[0].x *= 0.5f * (float)ScreenWidth();
				triProjected.p[0].y *= 0.5f * (float)ScreenHeight();
				triProjected.p[1].x *= 0.5f * (float)ScreenWidth();
				triProjected.p[1].y *= 0.5f * (float)ScreenHeight();
				triProjected.p[2].x *= 0.5f * (float)ScreenWidth();
				triProjected.p[2].y *= 0.5f * (float)ScreenHeight();

				olc::Pixel pixel;
				pixel.r = triProjected.colour[0];
				pixel.g = triProjected.colour[1];
				pixel.b = triProjected.colour[2];


				FillTriangle( triProjected.p[0].x, triProjected.p[0].y, 
							triProjected.p[1].x, triProjected.p[1].y, 
							triProjected.p[2].x, triProjected.p[2].y, pixel);

				DrawTriangle( triProjected.p[0].x, triProjected.p[0].y, 
							triProjected.p[1].x, triProjected.p[1].y, 
							triProjected.p[2].x, triProjected.p[2].y, olc::RED);				
			}
		}

		return true;
	}
};

int main()
{
	
	olcEngine3D demo;
	if (demo.Construct(1280, 720, 1, 1))
		demo.Start();
	return 0;
}