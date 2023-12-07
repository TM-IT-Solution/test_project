using UnityEngine;

public class PaddleController : MonoBehaviour
{
    public float speed = 5f;

    void Update()
    {
        // Move the paddle based on user input
        float horizontalInput = Input.GetAxis("Horizontal");
        transform.Translate(new Vector3(horizontalInput, 0, 0) * speed * Time.deltaTime);

        // Limit paddle movement within the screen boundaries
        float xPos = Mathf.Clamp(transform.position.x, -8f, 8f);
        transform.position = new Vector3(xPos, transform.position.y, transform.position.z);
    }
}
