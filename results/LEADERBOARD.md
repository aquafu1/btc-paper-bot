# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 249 windows, 6525 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 645 | 55.7 | 52.2 | $+155.92 | +2.4% | $1155.92 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 519 | 53.8 | 52.2 | $-57.36 | -1.1% | $942.64 | -0.3 | done | can't tell from luck |
| value_ev20 | 116 | 33.6 | 36.7 | $-140.27 | -12.1% | $859.73 | -1.0 | Sun 10:30 AM | too few trades (116/200) |
| value_ev10 | 313 | 36.7 | 40.8 | $-423.26 | -13.5% | $576.74 | -2.1 | done | losing for real |
| trend_filter | 343 | 46.1 | 50.5 | $-439.72 | -12.8% | $560.28 | -2.4 | done | losing for real |
| value_ev5 | 461 | 39.0 | 42.5 | $-565.11 | -12.3% | $434.89 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 519 | 46.2 | 49.9 | $-619.15 | -11.9% | $380.85 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 988 | 50.3 | 51.6 | $-670.54 | -6.8% | $329.46 | -2.2 | done | losing for real |
| coinflip | 988 | 49.3 | 50.9 | $-758.73 | -7.7% | $241.27 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 645 | 44.3 | 49.9 | $-973.26 | -15.1% | $26.74 | -3.9 | done | losing for real |
| always_up | 988 | 47.0 | 50.5 | $-1135.06 | -11.5% | $-135.06 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1463 | 46.5 | 49.8 | $-1539.50 |
| ETH | 1627 | 46.8 | 49.1 | $-1676.94 |
| SOL | 1689 | 48.1 | 49.4 | $-1404.12 |
| XRP | 1746 | 48.6 | 49.2 | $-1005.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
