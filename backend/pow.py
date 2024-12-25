import hashlib
import secrets
import string
import uuid

from typing import Annotated
from fastapi import Depends, HTTPException

proofs = {}

HARDNESS = 8
SIZE = 10

def _get_proof(user: str, proof: str):
    if user in proofs:
        if proofs[user] == proof:
            return user
    
    raise HTTPException(status_code=403, detail="nope")

def _gen_random_sequence() -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(SIZE))


def generate_proof(user: str):
    proof: str = _gen_random_sequence()
    proofs[user] = proof
    print(user, proof)
    return (proof[:HARDNESS], hashlib.sha256(hashlib.sha256(proof.encode("utf-8")).hexdigest().encode("utf-8")).hexdigest(), SIZE)

PROOF = Annotated[str, Depends(_get_proof)]