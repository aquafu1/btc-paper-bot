# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 347 windows, 9314 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:30 PM | too few trades (184/200) |
| value_ev10 | 455 | 40.2 | 40.3 | $-179.48 | -3.9% | $820.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 673 | 41.8 | 42.0 | $-300.46 | -4.5% | $699.54 | -1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 754 | 51.5 | 52.1 | $-367.62 | -4.9% | $632.38 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 923 | 51.8 | 52.0 | $-415.84 | -4.5% | $584.16 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 754 | 48.5 | 49.6 | $-472.71 | -6.3% | $527.29 | -1.7 | done | can't tell from luck |
| trend_filter | 508 | 47.0 | 50.2 | $-518.60 | -10.2% | $481.40 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 923 | 48.2 | 49.7 | $-639.25 | -6.9% | $360.75 | -2.1 | done | losing for real |
| coinflip | 1380 | 50.3 | 50.8 | $-657.35 | -4.8% | $342.65 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 1380 | 48.8 | 51.3 | $-1160.96 | -8.4% | $-160.96 | -3.2 | done | losing for real |
| always_up | 1380 | 46.5 | 50.6 | $-1612.77 | -11.7% | $-612.77 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2090 | 47.0 | 49.3 | $-1744.13 |
| ETH | 2343 | 47.5 | 48.7 | $-1688.97 |
| SOL | 2414 | 48.0 | 49.3 | $-1791.12 |
| XRP | 2467 | 48.8 | 49.1 | $-1139.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
