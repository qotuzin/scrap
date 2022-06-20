#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine.h"

struct Hex
{
    const int q, r, s;
    Hex(int q_, int r_, int s_): q(q_), r(r_), s(s_) {}
};

struct FractionalHex
{
    const float q, r, s;
    FractionalHex(float q_, float r_, float s_): q(q_), r(r_), s(s_) {}
};

struct Orientation
{ // Holds all the constants required to translate hex coordinates to screen coordinates
    const double f0, f1, f2 ,f3;
    const double b0, b1, b2, b3;
    const double start_angle; // in multiples of 60°
    Orientation(double f0_, double f1_, double f2_, double f3_,
                double b0_, double b1_, double b2_, double b3_,
                double start_angle_)
    : f0(f0_), f1(f1_), f2(f2_), f3(f3_),
      b0(b0_), b1(b1_), b2(b2_), b3(b3_),
      start_angle(start_angle_) {}
};

struct Point
{
    double x, y;
    Point(double x_, double y_): x(x_), y(y_) {}
};

struct Layout
{
    const Orientation orientation;
    const Point origin;
    Point size;
    Layout(Orientation orientation_, Point size_, Point origin_)
    : orientation(orientation_), origin(origin_), size(size_) {}
};

struct HexGrid
{
    std::vector<Hex> hexes = {};

    HexGrid()
    {
        for (int q = 0; q < 10; q++)
        {
            for (int r = 0; r < 10; r++)
            {
                hexes.push_back(Hex( q, r, 0));
            }
        }
    }
};


Point hex_to_pixel(Layout layout, Hex hex)
{
    const Orientation& M = layout.orientation;
    double x = (M.f0 * hex.q + M.f1 * hex.r) * layout.size.x;
    double y = (M.f2 * hex.q + M.f3 * hex.r) * layout.size.y;
    return Point(x + layout.origin.x, y + layout.origin.y);
}

FractionalHex pixel_to_hex(Layout layout, Point point)
{
    const Orientation& M = layout.orientation;
    Point pt = Point(( point.x - layout.origin.x) / layout.size.x,
                    ( point.y - layout.origin.y) / layout.size.y );
    double q = M.b0 * pt.x + M.b1 * pt.y;
    double r = M.b2 * pt.x + M.b1 * pt.y;
    return FractionalHex(q, r, -q - r);
};


Point hex_corner_offset(Layout layout, int corner)
{
    Point size = layout.size;
    double angle = 2.0 * M_PI * (layout.orientation.start_angle + corner) / 6;
    return Point(size.x * cos(angle), size.y * sin(angle));
}

std::vector<Point> polygon_corners(Layout layout, Hex hex)
{
    std::vector<Point> corners = {};
    Point centre = hex_to_pixel(layout, hex);
    for (int i  = 0; i < 6; i++)
    {
        Point offset = hex_corner_offset(layout, i);
        corners.push_back(Point(centre.x + offset.x, centre.y + offset.y));
    }
    return corners;
}










// MAIN CLASS
class olcEngine : public olc::PixelGameEngine
{
public:
    olcEngine()
    {
        sAppName = "HEX DEMO";
    }

public:
    const Orientation layout_pointy
        = Orientation( sqrt(3.0), sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0,
                       sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0,
                       0.5);

        const Orientation layout_flat
            = Orientation( 3.0 / 2.0, 0.0,sqrt(3) / 2.0, sqrt(3.0),
                           2.0 / 3.0, 0.0, -1.0 / 3.0, sqrt(3.0) / 3.0,
                           0.0);

    Point layout_origin = Point(050, 050);
    Point layout_size = Point(20, 15);
    Layout hex_layout = Layout(layout_flat, layout_size, layout_origin);

    int initMousePosX = 0;
    int initMousePosY = 0;

    //Hex hexagon = Hex(0,0,0);
    HexGrid hexagons = HexGrid();

    int DrawHex(Layout layout, Hex hex) 
    {

        std::vector<Point> corners = polygon_corners(layout, hex);
        for (int i = 0; i < 5; i++)
        {

            DrawLine(corners[i].x, corners[i].y, corners[i + 1].x, corners[i + 1].y);
        }
        DrawLine(corners[5].x, corners[5].y, corners[0].x, corners[0].y);

        return 0;
    }





    bool OnUserCreate() override
    { // Called once on startup

        int initPosX;
        int initPosY;

        return true;
    }

    bool OnUserUpdate(float fElapsedTime) override
    { // Called every frame

        FillRect(0, 0, 500, 500, olc::BLACK);

        if (GetMouse(0).bPressed)
        {
           initMousePosX = GetMouseX();
           initMousePosY = GetMouseY();
        }

        if (GetMouse(0).bHeld)
            {
                DrawRect(initMousePosX, initMousePosY, GetMouseX() - initMousePosX, GetMouseY() - initMousePosY, olc::YELLOW);
            }

        if (GetMouseWheel() > 0)
        { // Zoom in
            hex_layout.size.x += 4;
            hex_layout.size.y += 3;

        }

        if (GetMouseWheel() < 0)
        { // Zoom out
            hex_layout.size.x -= 4;
            hex_layout.size.y -= 3;

        }

        for (int i = 0; i < hexagons.hexes.size(); i++)
        {
            DrawHex(hex_layout, hexagons.hexes[i]);
        }

        DrawCircle(GetMouseX(), GetMouseY(), 4, olc::YELLOW);

        return true;

    }
};







int main()
{
    olcEngine demo;
    if (demo.Construct(500, 500, 1, 1))
        demo.Start();
}
#include <vector>
