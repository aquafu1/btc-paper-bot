# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 691 windows, 19124 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 368 | 34.0 | 34.9 | $-262.42 | -7.1% | $737.58 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1615 | 50.3 | 49.5 | $-444.40 | -2.8% | $555.60 | -1.1 | done | can't tell from luck |
| value_ev10 | 887 | 38.2 | 39.1 | $-548.58 | -6.2% | $451.42 | -1.5 | done | can't tell from luck |
| trend_filter | 1115 | 50.4 | 50.9 | $-587.43 | -5.3% | $412.57 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1963 | 51.3 | 50.8 | $-635.09 | -3.2% | $364.91 | -1.4 | done | can't tell from luck |
| value_ev5 | 1330 | 40.7 | 41.1 | $-648.70 | -4.9% | $351.30 | -1.5 | done | can't tell from luck |
| coinflip | 2756 | 50.1 | 50.3 | $-1230.92 | -4.5% | $-230.92 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1615 | 49.7 | 51.3 | $-1257.86 | -7.8% | $-257.86 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1963 | 48.7 | 50.0 | $-1283.72 | -6.5% | $-283.72 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2756 | 50.8 | 51.8 | $-1529.08 | -5.5% | $-529.08 | -3.0 | done | losing for real |
| always_up | 2756 | 47.5 | 49.6 | $-2314.43 | -8.4% | $-1314.43 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4341 | 48.2 | 49.1 | $-2523.30 |
| ETH | 4765 | 48.3 | 48.5 | $-2773.04 |
| SOL | 4980 | 48.1 | 48.6 | $-2932.17 |
| XRP | 5038 | 48.5 | 48.3 | $-2514.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
