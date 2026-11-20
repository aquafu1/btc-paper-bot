# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 889 windows, 24526 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1125 | 38.2 | 39.1 | $-611.54 | -5.4% | $388.46 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2070 | 50.0 | 49.8 | $-910.72 | -4.4% | $89.28 | -2.0 | done | losing for real |
| trend_filter | 1445 | 50.0 | 51.0 | $-971.24 | -6.7% | $28.76 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2505 | 50.5 | 50.4 | $-993.61 | -4.0% | $6.39 | -2.0 | done | can't tell from luck |
| value_ev5 | 1701 | 39.8 | 41.0 | $-1048.51 | -6.2% | $-48.51 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2070 | 50.0 | 50.9 | $-1376.55 | -6.6% | $-376.55 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2505 | 49.5 | 50.4 | $-1409.90 | -5.6% | $-409.90 | -2.8 | done | losing for real |
| coinflip | 3548 | 50.3 | 50.3 | $-1518.31 | -4.3% | $-518.31 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3548 | 51.3 | 51.7 | $-1619.71 | -4.6% | $-619.71 | -2.8 | done | losing for real |
| always_up | 3548 | 46.9 | 49.6 | $-3469.01 | -9.8% | $-2469.01 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5591 | 48.3 | 49.1 | $-3038.67 |
| ETH | 6107 | 48.2 | 48.5 | $-3811.54 |
| SOL | 6400 | 48.2 | 48.5 | $-3612.60 |
| XRP | 6428 | 48.4 | 48.5 | $-3565.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
