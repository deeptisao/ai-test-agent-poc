# AI Test Agent POC

This project demonstrates end-to-end automated test generation
from FastAPI OpenAPI specs using open-source LLMs.

Pipeline:
Code → OpenAPI → Postman → AI Test Gen → CI Execution

Stack:
- FastAPI
- Python
- Open models (DeepSeek / Qwen)
- AWS (EC2, S3)
- GitHub Actions

This is a POC that can be evolved into a product.
