# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 409 windows, 11198 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 955 | 51.0 | 49.9 | $-191.49 | -2.0% | $808.51 | -0.6 | done | can't tell from luck |
| value_ev10 | 524 | 40.3 | 40.5 | $-203.49 | -3.9% | $796.51 | -0.7 | done | can't tell from luck |
| value_ev5 | 790 | 42.0 | 42.2 | $-312.64 | -4.0% | $687.36 | -1.0 | done | can't tell from luck |
| trend_filter | 634 | 50.2 | 50.7 | $-313.07 | -4.9% | $686.93 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1127 | 49.4 | 49.9 | $-506.43 | -4.5% | $493.57 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1127 | 50.6 | 51.9 | $-720.56 | -6.4% | $279.44 | -2.3 | done | losing for real |
| coinflip | 1628 | 50.1 | 50.9 | $-823.41 | -5.1% | $176.59 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 955 | 49.0 | 52.0 | $-894.80 | -9.4% | $105.20 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1628 | 49.9 | 51.6 | $-1094.42 | -6.7% | $-94.42 | -2.8 | done | losing for real |
| always_up | 1628 | 45.7 | 50.7 | $-2148.52 | -13.2% | $-1148.52 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2529 | 47.6 | 49.5 | $-1816.06 |
| ETH | 2814 | 47.9 | 49.0 | $-1727.77 |
| SOL | 2896 | 47.9 | 49.5 | $-2204.19 |
| XRP | 2959 | 48.9 | 49.3 | $-1547.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
