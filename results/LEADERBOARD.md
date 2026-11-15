# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 394 windows, 10797 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 198 | 36.9 | 36.5 | $-46.95 | -2.4% | $953.05 | -0.3 | Sat 11:45 PM | too few trades (198/200) |
| value_ev10 | 514 | 40.5 | 40.5 | $-165.67 | -3.2% | $834.33 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 915 | 50.7 | 49.8 | $-209.06 | -2.3% | $790.94 | -0.7 | done | can't tell from luck |
| value_ev5 | 761 | 42.0 | 42.1 | $-281.20 | -3.7% | $718.80 | -0.9 | done | can't tell from luck |
| trend_filter | 613 | 49.8 | 50.6 | $-342.33 | -5.6% | $657.67 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1087 | 49.0 | 49.8 | $-532.69 | -4.9% | $467.31 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1087 | 51.0 | 52.1 | $-640.37 | -5.9% | $359.63 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 915 | 49.3 | 52.1 | $-830.27 | -9.1% | $169.73 | -2.9 | done | losing for real |
| coinflip | 1569 | 49.9 | 50.9 | $-842.12 | -5.4% | $157.88 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1569 | 49.8 | 51.6 | $-1052.99 | -6.7% | $-52.99 | -2.7 | done | losing for real |
| always_up | 1569 | 46.5 | 50.7 | $-1851.09 | -11.8% | $-851.09 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2440 | 47.7 | 49.5 | $-1660.40 |
| ETH | 2712 | 48.0 | 48.9 | $-1644.89 |
| SOL | 2789 | 48.0 | 49.5 | $-2050.44 |
| XRP | 2856 | 48.9 | 49.2 | $-1439.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
