# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 160 windows, 4072 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 297 | 58.9 | 53.4 | $+233.44 | +7.9% | $1233.44 | +1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 393 | 56.5 | 52.6 | $+185.84 | +4.7% | $1185.84 | +1.0 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 4:30 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 632 | 51.9 | 51.2 | $-181.84 | -2.9% | $818.16 | -0.7 | done | can't tell from luck |
| value_ev10 | 206 | 37.9 | 40.9 | $-253.71 | -12.3% | $746.29 | -1.5 | done | can't tell from luck |
| coinflip | 632 | 50.8 | 50.9 | $-298.75 | -4.7% | $701.25 | -1.2 | done | can't tell from luck |
| trend_filter | 209 | 41.6 | 48.8 | $-373.00 | -17.8% | $627.00 | -2.6 | done | losing for real |
| value_ev5 | 304 | 38.8 | 42.6 | $-405.87 | -13.4% | $594.13 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 297 | 41.1 | 48.9 | $-560.98 | -18.9% | $439.02 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 393 | 43.5 | 49.7 | $-611.88 | -15.6% | $388.12 | -3.1 | done | losing for real |
| always_up | 632 | 45.6 | 50.4 | $-877.68 | -13.9% | $122.32 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 884 | 46.3 | 49.6 | $-763.93 |
| ETH | 1013 | 45.6 | 48.9 | $-1158.19 |
| SOL | 1069 | 47.9 | 49.0 | $-884.27 |
| XRP | 1106 | 50.1 | 49.2 | $-436.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
