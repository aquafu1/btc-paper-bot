# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 949 windows, 26324 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 485 | 35.3 | 34.8 | $-134.35 | -2.8% | $865.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1195 | 38.2 | 39.1 | $-618.29 | -5.2% | $381.71 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2691 | 51.2 | 50.6 | $-794.89 | -3.0% | $205.11 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2253 | 50.2 | 49.7 | $-863.20 | -3.8% | $136.80 | -1.8 | done | can't tell from luck |
| trend_filter | 1571 | 50.0 | 50.8 | $-998.86 | -6.4% | $1.14 | -2.6 | done | losing for real |
| value_ev5 | 1815 | 39.9 | 41.0 | $-1012.07 | -5.6% | $-12.07 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 2253 | 49.8 | 51.0 | $-1626.59 | -7.2% | $-626.59 | -3.5 | done | losing for real |
| coinflip | 3790 | 50.2 | 50.4 | $-1688.63 | -4.5% | $-688.63 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2691 | 48.8 | 50.2 | $-1828.86 | -6.8% | $-828.86 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3790 | 50.9 | 51.5 | $-1872.07 | -4.9% | $-872.07 | -3.1 | done | losing for real |
| always_up | 3790 | 46.8 | 49.6 | $-3746.48 | -9.9% | $-2746.48 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5999 | 48.2 | 49.0 | $-3385.26 |
| ETH | 6544 | 48.2 | 48.5 | $-3978.91 |
| SOL | 6866 | 48.3 | 48.6 | $-3779.54 |
| XRP | 6915 | 48.3 | 48.5 | $-4040.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
