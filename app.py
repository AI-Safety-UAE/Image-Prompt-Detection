from ui import create_interface


demo = create_interface()

if __name__ == "__main__":
    # We can remove the server_name and server_port arguments here,
    # as they are now handled by the command in docker-compose.yml
    demo.launch(server_name="0.0.0.0", server_port=7860)