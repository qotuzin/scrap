#include <iostream>
#include "include/Game.h"

int main ()
{
    //Init Game engine
    Game game;

    // Game loop
    while(game.getWindowIsOpen())
    {
        // Update
        game.update();

        // Render
        game.render();
    }

    //End of application
    return 0;
}
