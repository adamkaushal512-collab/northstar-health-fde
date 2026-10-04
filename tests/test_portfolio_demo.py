from subprocess import run
import sys

def test_demo_runs():
    result=run([sys.executable,"scripts/demo.py","AUTH-1001"],capture_output=True,text=True)
    assert result.returncode==0
    assert "NORTHSTAR HEALTH" in result.stdout
    assert "Human review required: True" in result.stdout
    assert "BOUNDED TOOL TRACE" in result.stdout
