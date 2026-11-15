# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 397 windows, 10892 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:00 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 924 | 50.5 | 49.8 | $-242.21 | -2.6% | $757.79 | -0.8 | done | can't tell from luck |
| value_ev5 | 769 | 42.0 | 42.2 | $-300.26 | -3.9% | $699.74 | -0.9 | done | can't tell from luck |
| trend_filter | 617 | 49.8 | 50.6 | $-345.16 | -5.6% | $654.84 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1096 | 49.2 | 49.8 | $-515.09 | -4.7% | $484.91 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1096 | 50.8 | 52.0 | $-673.79 | -6.1% | $326.21 | -2.1 | done | losing for real |
| coinflip | 1583 | 50.0 | 50.8 | $-805.62 | -5.1% | $194.38 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 924 | 49.5 | 52.1 | $-811.35 | -8.8% | $188.65 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1583 | 49.8 | 51.6 | $-1069.98 | -6.8% | $-69.98 | -2.8 | done | losing for real |
| always_up | 1583 | 46.2 | 50.8 | $-1944.00 | -12.3% | $-944.00 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2466 | 47.7 | 49.5 | $-1715.87 |
| ETH | 2727 | 48.0 | 48.9 | $-1672.06 |
| SOL | 2820 | 48.0 | 49.5 | $-2100.52 |
| XRP | 2879 | 48.9 | 49.2 | $-1440.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
