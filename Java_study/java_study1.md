# Java1

### 형 변환(Type Casting)

변수의 타입을 다른 타입으로 변환하는 것  

primitive <-> primitive, reference <-> reference  
- boolean은 다른 기본 타입과 호환되지 않음  
- 기본 타입과 참조형의 형 변환을 위해서 Wrapper 클래스 사용  

```java
// ex
double d = 100.5;
int reuslt = (int) d;
```

```java
// 묵시적 형 변환(promotion)

byte b = 10;
int i = (int) b;
int i2 = b;
```

```java
// 명시적 형 변환  

int i = 300;
byte b = (byte) i;
```



### 다음 코드 분석하기

```java
import java.io.IOException;
import java.io.InputStream;

class MagicianShark_230403 {
    static class Fireball {

        private static final int[][] OFFSET = {
                {-1,0}, {-1,1}, {0,1},
                {1,1}, {1,0}, {1,-1},
                {0,-1}, {-1,-1}
        };
        private static int N;
        private int r, c, m, s, d, cnt;

        Fireball(int[] fireball) {
            r = fireball[0];
            c = fireball[1];
            m = fireball[2];
            s = fireball[3];
            d = fireball[4];
            cnt = 1;
        }

        public void move() {
            r = (r + OFFSET[d][0]*s) % N;
            if (r < 0) {
                r += N;
            }
            c = (c + OFFSET[d][1]*s) % N;
            if (c < 0) {
                c += N;
            }
        }

        public void add(Fireball fb) {
            m += fb.m;
            s += fb.s;
            d = (d % 2 != fb.d % 2) ? -1 : d % 2;
            cnt++;
        }
    }

    private int N;
    private Fireball[][] board;

    public int getSumMassAfter(int N, int K, int[][] fireballs) {
        this.N = Fireball.N = N;
        board = new Fireball[N][N];
        for (int[] fireball : fireballs) {
            fireball[0]--;
            fireball[1]--;
            Fireball fb = new Fireball(fireball);
            board[fb.r][fb.c] = fb;
        }

        for (int i = 0; i < K; ++i) {
            separateAndMoveAndAssembleFireballs();
            destroyFireballs();
        }
        return getSumMass();
    }

    private void separateAndMoveAndAssembleFireballs() {
        Fireball[][] newBoard = new Fireball[N][N];
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                Fireball fb = board[r][c];
                if (fb == null) {
                    continue;
                }

                if (fb.cnt == 1) {
                    moveOneFireball(fb, newBoard);
                } else {
                    separateFireballAndMoveOnes(fb, newBoard);
                }
            }
        }
        board = newBoard;
    }

    private void moveOneFireball(Fireball fb, Fireball[][] newBoard) {
        fb.move();
        int nr = fb.r;
        int nc = fb.c;
        Fireball fbFirst = newBoard[nr][nc];
        if (fbFirst == null) {
            newBoard[nr][nc] = fb;
        } else {
            fbFirst.add(fb);
        }
    }

    private void separateFireballAndMoveOnes(Fireball fb, Fireball[][] newBoard) {
        int r = fb.r;
        int c = fb.c;
        int nm = fb.m / 5;
        int ns = fb.s / fb.cnt;
        int nd = (fb.d == -1) ? 1 : 0;

        for (int i = 0; i < 4; ++i) {
            fb = new Fireball(new int[] {r, c, nm, ns, nd+2*i});
            moveOneFireball(fb, newBoard);
        }
    }

    private void destroyFireballs() {
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                Fireball fb = board[r][c];
                if (fb == null) {
                    continue;
                }

                if (fb.cnt > 1 && fb.m / 5 == 0) {
                    board[r][c] = null;
                }
            }
        }
    }

    private int getSumMass() {
        int sum = 0;
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                Fireball fb = board[r][c];
                if (fb == null) {
                    continue;
                }

                sum += (fb.cnt == 1) ? fb.m : 4 * (fb.m / 5);
            }
        }
        return sum;
    }

}

public class Main {

    static InputStream IN = System.in;

    public static void main(String[] args) throws IOException {
        int N = readInt();
        int M = readInt();
        int K = readInt();
        int[][] fireballs = new int[M][5];
        for (int i = 0; i < M; ++i) {
            int[] fireball = fireballs[i];
            for (int j = 0; j < 5; ++j) {
                fireball[j] = readInt();
            }
        }
        int ans = new MagicianShark_230403().getSumMassAfter(N, K, fireballs);
        System.out.println(ans);
    }

    private static int readInt() throws IOException {
        int val = 0;
        do {
            int ch = IN.read();
            if (ch == ' ' || ch == '\n') break;
            val = 10*val + ch-48;
        } while (true);
        return val;
    }

}

```