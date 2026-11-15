# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 437 windows, 12029 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1026 | 51.0 | 49.9 | $-208.16 | -2.0% | $791.84 | -0.7 | done | can't tell from luck |
| trend_filter | 693 | 49.9 | 50.5 | $-360.97 | -5.2% | $639.03 | -1.4 | done | can't tell from luck |
| value_ev10 | 565 | 38.9 | 40.2 | $-383.63 | -6.8% | $616.37 | -1.3 | done | can't tell from luck |
| value_ev5 | 843 | 41.2 | 41.9 | $-479.11 | -5.7% | $520.89 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1218 | 49.6 | 50.0 | $-539.56 | -4.4% | $460.44 | -1.5 | done | can't tell from luck |
| coinflip | 1740 | 50.4 | 50.9 | $-809.01 | -4.6% | $190.99 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1218 | 50.4 | 51.7 | $-827.72 | -6.8% | $172.28 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1026 | 49.0 | 51.9 | $-996.12 | -9.7% | $3.88 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1740 | 49.7 | 51.5 | $-1247.75 | -7.2% | $-247.75 | -3.1 | done | losing for real |
| always_up | 1740 | 46.0 | 50.5 | $-2206.46 | -12.7% | $-1206.46 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2715 | 47.5 | 49.3 | $-2104.52 |
| ETH | 3021 | 48.0 | 48.8 | $-1886.73 |
| SOL | 3123 | 47.8 | 49.3 | $-2458.84 |
| XRP | 3170 | 48.6 | 49.2 | $-1786.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
