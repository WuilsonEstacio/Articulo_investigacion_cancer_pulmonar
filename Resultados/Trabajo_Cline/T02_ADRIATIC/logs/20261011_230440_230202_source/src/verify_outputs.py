"""Hash deterministic deliverables; optionally compare a preserved manifest."""
import argparse
import hashlib
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--compare',type=Path)
    args=parser.parse_args()
    files=[p for folder in ['src','tests','config','data_derived','figures'] for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    files.extend(ROOT.glob('*.md'))
    files.append(ROOT/'requirements_T02.txt')
    frame=pd.DataFrame([dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in sorted(files)])
    if args.compare:
        before=pd.read_csv(args.compare).set_index('path').sha256
        after=frame.set_index('path').sha256
        differences=before.to_frame('before').join(after.rename('after'),how='outer')
        differences=differences[differences.before!=differences.after]
        print('Manifest differences:',len(differences),flush=True)
        if len(differences):
            print(differences.to_string())
            raise RuntimeError('Deliverables differ from baseline')
    frame.to_csv(ROOT/'manifest_sha256.csv',index=False)
    print('Verified/hash-listed files:',len(frame),flush=True)


if __name__=='__main__':
    main()