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
    filter = seccomp.SyscallFilter(seccomp.ERRNO(seccomp.errno.EPERM))
    filter.add_rule(seccomp.KILL, "write", seccomp.Arg(0, seccomp.EQ, sys.stdout.fileno()))
    filter.load()

    # Exécution de la commande
    command = sys.argv[1:]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
