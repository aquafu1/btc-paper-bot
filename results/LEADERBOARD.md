# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 516 windows, 14239 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 268 | 34.3 | 35.5 | $-194.82 | -7.3% | $805.18 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1211 | 51.1 | 49.8 | $-204.77 | -1.7% | $795.23 | -0.6 | done | can't tell from luck |
| value_ev10 | 666 | 38.1 | 39.7 | $-496.88 | -7.5% | $503.12 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1445 | 49.7 | 49.6 | $-583.49 | -4.0% | $416.51 | -1.5 | done | can't tell from luck |
| trend_filter | 836 | 49.3 | 50.7 | $-596.88 | -7.1% | $403.12 | -2.1 | done | losing for real |
| value_ev5 | 989 | 39.9 | 41.5 | $-723.60 | -7.3% | $276.40 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1445 | 50.3 | 51.6 | $-964.66 | -6.7% | $35.34 | -2.6 | done | losing for real |
| coinflip | 2056 | 50.0 | 50.7 | $-1087.69 | -5.3% | $-87.69 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1211 | 48.9 | 51.4 | $-1110.77 | -9.2% | $-110.77 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2056 | 49.4 | 51.6 | $-1657.63 | -8.1% | $-657.63 | -3.8 | done | losing for real |
| always_up | 2056 | 46.4 | 50.1 | $-2334.74 | -11.4% | $-1334.74 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3225 | 47.2 | 49.2 | $-2692.52 |
| ETH | 3557 | 47.9 | 48.7 | $-2431.84 |
| SOL | 3709 | 47.7 | 49.0 | $-2683.14 |
| XRP | 3748 | 48.4 | 48.8 | $-2148.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
