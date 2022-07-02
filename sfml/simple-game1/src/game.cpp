#include <iostream>
#include "include/Game.h"

//Private Functions
void Game::initVariables()
{
    this->window = nullptr;
}

void::Game::initWindow()
{
    this->videoMode.height = 600;
    this->videoMode.width = 800;
    
    this->window = new sf::RenderWindow(this->videoMode, "Simple Game 1", sf::Style::Titlebar | sf::Style::Close);

    this->window->setFramerateLimit(144);
}

void::Game::initEnemies()
{
    this->enemy.setPosition(sf::Vector2f(100.f, 100.f));
    this->enemy.setSize(sf::Vector2f(100.f, 100.f));
    this->enemy.setFillColor(sf::Color::Cyan);
    this->enemy.setOutlineColor(sf::Color::Green);
    this->enemy.setOutlineThickness(5.f);
}

//Constructors / Destructors
Game::Game()
{
    this->initVariables();
    this->initWindow();
    initEnemies();

}

Game::~Game()
{
    delete this->window;

}

//Accessors
const bool Game::getWindowIsOpen() const
{
    return this->window->isOpen();
}

//Functions
void Game::pollEvents()
{
    //Event polling
    while(this->window->pollEvent(this->event)) {
        switch(this->event.type) {
            case sf::Event::Closed:
                this->window->close();
                break;
            case sf::Event::KeyPressed:
                if (event.key.code == sf::Keyboard::Escape)
                    this->window->close();
                if (event.key.code == sf::Keyboard::Q)
                    this->window->close();
                break;
        }
    }

}

void Game::update()
{
    pollEvents();

    //Update mouse position
    std::cout << "Mouse pos: " << sf::Mouse::getPosition(*this->window).x << ", " << sf::Mouse::getPosition(*this->window).y << std::endl;

}

void Game::render()
{
    /*
        @return void
        - clear old frame
        - render objects
        - display frame in window

        Renders the game objects.
    */

    this->window->clear();

    //Draw game objects
    this->window->draw(this->enemy);
    
    this->window->display();
}
