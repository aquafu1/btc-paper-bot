# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 263 windows, 6888 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 683 | 55.3 | 52.2 | $+131.28 | +1.9% | $1131.28 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 551 | 53.4 | 52.2 | $-103.41 | -1.9% | $896.59 | -0.5 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 12:30 PM | too few trades (120/200) |
| value_ev10 | 327 | 36.1 | 40.8 | $-479.85 | -14.7% | $520.15 | -2.3 | done | losing for real |
| trend_filter | 359 | 45.7 | 50.3 | $-485.27 | -13.5% | $514.73 | -2.6 | done | losing for real |
| value_ev5 | 482 | 39.0 | 42.4 | $-580.76 | -12.0% | $419.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 551 | 46.6 | 49.8 | $-614.39 | -11.2% | $385.61 | -2.7 | done | losing for real |
| coinflip | 1044 | 49.3 | 50.8 | $-777.05 | -7.4% | $222.95 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1044 | 49.6 | 51.5 | $-830.05 | -8.0% | $169.95 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 683 | 44.7 | 49.8 | $-973.13 | -14.2% | $26.87 | -3.8 | done | losing for real |
| always_up | 1044 | 47.7 | 50.2 | $-982.32 | -9.4% | $17.68 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1540 | 46.4 | 49.5 | $-1634.98 |
| ETH | 1716 | 46.7 | 49.1 | $-1721.65 |
| SOL | 1785 | 48.0 | 49.3 | $-1483.36 |
| XRP | 1847 | 48.8 | 49.2 | $-1006.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
