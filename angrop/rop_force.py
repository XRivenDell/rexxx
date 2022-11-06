from ropgadget.core import Core 
from ropgadget.args import Args

def GetAddrFromROPgadget(path):

  s = ["--binary",path,"--silent","--dump"]
  args = Args(arguments=s)
  core = Core(args.getArgs())
  core.analyze()
  gs = core.gadgets()
  addr = []
  for g in gs:
    addr.append((g['vaddr'],g['vaddr']+len(g['bytes'])))

  return addr

if __name__ == "__main__":
  fixpath = "/home/wsl/angr-dev/rex/my_binaries/vuln_stacksmash_withshell"
  GetAddrFromROPgadget(fixpath)
