import fastapi
import pydantic
import uuid

from pow import generate_proof, PROOF

app = fastapi.FastAPI()

class ProofRequest(pydantic.BaseModel):
    uuid: str
    proof: str
    hash: str
    target_len: int


@app.get("/request")
def request() -> ProofRequest:
    user = uuid.uuid4()

    proof, hash, size = generate_proof(user.hex)

    return ProofRequest(
        uuid=user.hex,
        proof=proof,
        hash=hash,
        target_len=size
    )

@app.get("/test")
def test(proof: PROOF) -> str:
    return proof