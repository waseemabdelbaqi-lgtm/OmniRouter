# Guide to testing

chat_model -> tests all chat models
image_model -> tests all image models
test_user -> tests a single model of your choice

# Setup

The live tests call real providers through Firestore auth. Set `OMNI_TEST_API_KEY` to a valid
OmniRouter key (see `.env.example`), along with the server's provider keys and Firebase credentials.
`test_messages.py` needs none of these; it runs offline.

# Run all tests
Run: `pytest`


# To test chat models

Run: `python -m pytest testLib/test_chat_model.py -v`


# To test image models

Run: `python -m pytest testLib/test_image.py -v`

# To test a single model

Run: `python -m testLib.test_user model_name`
