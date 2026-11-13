# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 206 windows, 5348 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 524 | 57.4 | 52.8 | $+289.19 | +5.5% | $1289.19 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 406 | 56.4 | 52.7 | $+155.05 | +3.8% | $1155.05 | +0.8 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 3:00 AM | too few trades (104/200) |
| value_ev10 | 269 | 36.4 | 40.8 | $-392.98 | -14.6% | $607.02 | -2.1 | done | losing for real |
| coinflip | 816 | 50.5 | 51.0 | $-430.86 | -5.3% | $569.14 | -1.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 816 | 50.7 | 51.4 | $-432.54 | -5.3% | $567.46 | -1.6 | done | can't tell from luck |
| trend_filter | 275 | 43.3 | 49.7 | $-447.28 | -16.3% | $552.72 | -2.7 | done | losing for real |
| value_ev5 | 392 | 38.5 | 42.5 | $-524.50 | -13.4% | $475.50 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 406 | 43.6 | 49.4 | $-637.57 | -15.7% | $362.43 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 524 | 42.6 | 49.5 | $-913.14 | -17.4% | $86.86 | -4.1 | done | losing for real |
| always_up | 816 | 45.5 | 50.2 | $-1117.55 | -13.7% | $-117.55 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1187 | 46.0 | 49.6 | $-1234.67 |
| ETH | 1334 | 46.3 | 48.8 | $-1319.89 |
| SOL | 1382 | 47.5 | 49.2 | $-1285.85 |
| XRP | 1445 | 49.1 | 49.2 | $-749.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
