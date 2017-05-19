#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
Collatz - 2017 - by psy (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with Collatz; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import os, sys
import matplotlib.pyplot as plt

class Collatz(object):
    def __init__(self):
        self.m=False

    def banner(self):
        print "  ____      _ _       _               "
        print " / ___|___ | | | __ _| |_ ____        "
        print "| |   / _ \| | |/ _` | __|_  /        "
        print "| |__| (_) | | | (_| | |_ / /         "
        print " \____\___/|_|_|\__,_|\__/___|        "
        print " 'Natural integers always becomes 1?' "
        print "\n", 75*"="
        print " - RULE 1: if n is 'even' then n = n/2"
        print " - RULE 2: if n is 'odd' then n = 3n+1"
        print 75*"=","\n"

    def generate_graph(self):
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            print "[Info] Generating 'plots' for number:", self.root
        if not os.path.exists("graphs/"):
            os.mkdir("graphs/")
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            print "\n   + Thread(s):", len(self.tree)
            print '     - Tree =', self.tree
        plt.figure()
        fig = plt.figure(1)
        ax = fig.add_subplot(111, facecolor='black')
        for t in self.tree:
            ax.scatter(self.tree.index(t)+1, t, color="red", s=2)
        header = '"Tree" for number '+str(self.root)+' to becomes 1'
        plt.title(header)
        plt.ylabel('Number(s)')
        plt.xlabel('Thread(s)')
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            plt.show()
        g = "graphs/"+self.root
        if not os.path.exists(g):
            os.mkdir(g)
            f = open(g+"/"+self.root+"-collatz_tree.txt", 'wb')
            fig.savefig(g+"/"+self.root+"-collatz_graph.png")
            f.write(str(self.tree))
            f.close
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                print "\n[Info] Generated 'tree' secuence at folder: "+g+"/\n"
        else:
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                print "\n[Info] You have this 'tree' secuence previously saved. Exiting...\n"
        ax.clear()

    def generate_forest(self, rng):
        srng = rng.split('-')
        try:
            x=int(srng[0])
            y=int(srng[1])
        except:
            print "\n[Error] Numbers on range should be integers (ex: 427-8981318). Aborting...\n"
            sys.exit(2)
        print "[Info] Generating 'forest' for range:", rng, "\n"
        if x < y:
            for i in range(x,y+1):
               n = i
               self.root = str(n)
               if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                   print "[Info] Generating 'tree' for number:", self.root
               self.generate_tree(n)
        else:
            for i in range(y,x+1):
               n = i
               self.root = str(n)
               print "[Info] Generating 'tree' for number:", self.root
               self.generate_tree(n)

    def generate_tree(self, n):
        t=0 # threads counter
        o=0 # odds counter
        e=0 # evens counter
        w=False # warning flag
        self.tree = []
        while True:
            t=t+1
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                print ""
            try:
                if int(n) != 1:
                    if int(n) <= 0:
                        self.m=True
                        print "[Error] First number should be always > 0. Aborting...\n"
                        sys.exit(2)
                    else:
                        self.m=False
                        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                            print "   + Thread:", t
                        self.tree.append(int(n))
                        if int(n) & 1:
                            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                print '     - Root =', n, "[odd]"
                            r=3*int(n)+1
                            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                print '     - New  =', r, '[3*'+str(n)+'+1='+str(r)+"]"
                            o=o+1
                        else:
                            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                print '     - Root =', n, "[even]"
                            r=int(n)/2
                            if int(r) == 1:
                                w=True
                            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                                print '     - New  =', r, "["+str(n)+'/2='+str(r)+"]"
                            e=e+1
                    n = r
                else:
                    if w is False:
                        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                            print "   + Thread:", t
                        self.tree.append(int(n))
                        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                            print '     - Root =', n, "[odd]"
                        r=3*int(n)+1
                        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                            print '     - New  =', r, '[3*'+str(n)+'+1='+str(r)+"]"
                        o=o+1
                        w = True
                        n = r
                    else:
                        break
            except:
                import random # generate pseudo-random number
                n=(random.randint(1,9999))
                print "[Error] First number should be an integer (ex: "+str(n)+"). Aborting...\n"
                m = True
                sys.exit(2)
        if self.m is False:
            print 100*"-"
            print "[Info] Number "+self.root+ " takes "+str(int(t)-1)+" threads using "+str(o)+" odds and "+str(e)+" evens to becomes 1"
            print 100*"-","\n"
            if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
                graph=raw_input("Wanna generate a 'graph'? (Y/n)")
                if graph == "n" or graph == "N":
                    print ""
                    sys.exit(2)
                else:
                    self.generate_graph()
            else:
                self.generate_graph()

    def run(self, opts=None):
        self.banner()
        self.mode=raw_input("Set mode: single random (default), manual, learning (S/m/l): ") 
        print 40*"-"
        if self.mode == "m" or self.mode == "M" or self.mode == "Manual" or self.mode == "manual": #mode manual
            n=raw_input("Set a number: ")
        elif self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn": #mode learning
            rng=raw_input("Set range (ex: 1-100 or 345-890 (PRESS ENTER = 1-100) (STOP = CTRL+z): ")
            if not rng:
                rng="1-100"
        else: # mode single random
            r=raw_input("Set a max range (ex: 9999999) (PRESS ENTER = 9): ")
            if not r:
                r=9
            import random # generate pseudo-random number
            n=(random.randint(1,int(r)))
        if not self.mode == "l" or self.mode == "L" or self.mode == "Learn" or self.mode == "learn":
            self.root = str(n)
            print " + Generating 'tree' for number:", self.root
            self.generate_tree(n)
        else:
            print 75*"="
            self.generate_forest(rng)
            print "[Info] 'Forest' correctly generated. Exiting...\n"

if __name__ == "__main__":
    app = Collatz()
    app.run()
