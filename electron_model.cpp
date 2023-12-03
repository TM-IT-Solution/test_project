#include <SFML/Graphics.hpp>
#include <cmath>

int main() {
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "Electron Visualization");
    window.setFramerateLimit(60);

    // Create an electron circle
    sf::CircleShape electron(10);
    electron.setFillColor(sf::Color::Blue);

    // Set the initial position of the electron
    float angle = 0;
    float radius = 100;

    // Main loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Update the position of the electron in a circular motion
        float x = 400 + radius * std::cos(angle);
        float y = 300 + radius * std::sin(angle);

        electron.setPosition(x - electron.getRadius(), y - electron.getRadius());

        // Increase the angle for the next frame
        angle += 0.03;

        // Clear the window
        window.clear(sf::Color::Black);

        // Draw the electron
        window.draw(electron);

        // Display the contents of the window
        window.display();
    }

    return 0;
}
