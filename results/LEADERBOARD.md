# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 407 windows, 11138 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 948 | 51.1 | 49.9 | $-174.71 | -1.8% | $825.29 | -0.6 | done | can't tell from luck |
| value_ev10 | 523 | 40.2 | 40.5 | $-214.41 | -4.1% | $785.59 | -0.8 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| value_ev5 | 787 | 41.8 | 42.2 | $-343.76 | -4.4% | $656.24 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1122 | 49.6 | 49.9 | $-475.36 | -4.2% | $524.64 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1122 | 50.4 | 51.9 | $-753.05 | -6.7% | $246.95 | -2.4 | done | losing for real |
| coinflip | 1620 | 50.1 | 50.9 | $-818.40 | -5.1% | $181.60 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 948 | 48.9 | 52.0 | $-907.29 | -9.6% | $92.71 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1620 | 49.9 | 51.6 | $-1086.58 | -6.7% | $-86.58 | -2.8 | done | losing for real |
| always_up | 1620 | 45.7 | 50.7 | $-2151.00 | -13.3% | $-1151.00 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2515 | 47.7 | 49.5 | $-1791.90 |
| ETH | 2797 | 47.9 | 48.9 | $-1761.99 |
| SOL | 2881 | 47.9 | 49.5 | $-2224.06 |
| XRP | 2945 | 48.9 | 49.3 | $-1538.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
