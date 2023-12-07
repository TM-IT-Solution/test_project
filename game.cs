using UnityEngine;

public class BallController : MonoBehaviour
{
    public float speed = 5f;

    void Update()
    {
        // Move the ball downward
        transform.Translate(Vector3.down * speed * Time.deltaTime);

        // Check if the ball falls below the screen
        if (transform.position.y < -5f)
        {
            // Reset the ball position at the top
            transform.position = new Vector3(Random.Range(-8f, 8f), 5f, 0);
        }
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        // Check if the ball collides with the paddle
        if (other.CompareTag("Paddle"))
        {
            // Reset the ball position at the top
            transform.position = new Vector3(Random.Range(-8f, 8f), 5f, 0);
        }
    }
}
