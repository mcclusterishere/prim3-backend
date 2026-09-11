# prim3-backend — legacy / retired service

This repository is retained for history only. It is **not** the backend for the current PRIM3 learning system.

Canonical architecture:

- PRIM3 content/canon: `mcclusterishere/Prim3`
- Course publication feed: `mcclusterishere/Prim3/learning/course/course-feed.json`
- Backend/control plane: `mcclusterishere/mccluster`
- Worker: `mccluster`
- API: `https://api.mccluster.org`
- Learner data: shared McCluster Supabase project `zmnhbrjyhxzhkxmhkexs`

Do not add auth, course progress, AI routing, databases, billing, or new endpoints here. New PRIM3 API work belongs in `workers/mccluster/src/prim3/` in the McCluster control repository.

The historical `main.py` is not a source of truth and should not receive new production traffic.

## Security note

A local `.env` file was previously committed to this repository and has now been removed from the current tree. Deleting it does **not** erase earlier Git history. Any credential that was ever stored in that file should be treated as exposed and rotated at its provider.
