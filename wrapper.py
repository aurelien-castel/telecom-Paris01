import sys
import subprocess
try:
    import seccomp
except ImportError:
    import pyseccomp as seccomp    

def main():
    if len(sys.argv) < 2:
        print("Usage: python wrapper.py <commande> [args...]")
        sys.exit(1)

    # Configuration du filtre seccomp
    ctx = seccomp.SyscallFilter(seccomp.ERRNO(seccomp.errno.EPERM))
    ctx.add_rule(seccomp.DENY, seccomp.SYS_open, arg0_match=seccomp.FilterRuleArg(2, seccomp.EQ, 0x2))
    ctx.load()

    # Exécution de la commande
    command = sys.argv[1:]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
