# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 566 windows, 15693 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1333 | 51.2 | 49.7 | $-261.17 | -2.0% | $738.83 | -0.7 | done | can't tell from luck |
| value_ev20 | 308 | 33.1 | 35.2 | $-345.22 | -11.2% | $654.78 | -1.5 | done | can't tell from luck |
| trend_filter | 910 | 50.3 | 51.1 | $-547.42 | -6.0% | $452.58 | -1.9 | done | can't tell from luck |
| value_ev10 | 745 | 37.4 | 39.4 | $-715.71 | -9.6% | $284.29 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1593 | 50.8 | 51.0 | $-811.51 | -5.1% | $188.49 | -2.1 | done | losing for real |
| value_ev5 | 1107 | 39.7 | 41.3 | $-897.45 | -8.1% | $102.55 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1593 | 49.2 | 49.9 | $-914.74 | -5.7% | $85.26 | -2.3 | done | losing for real |
| coinflip | 2257 | 49.8 | 50.5 | $-1256.13 | -5.6% | $-256.13 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1333 | 48.8 | 51.2 | $-1302.92 | -9.8% | $-302.92 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2257 | 50.2 | 51.9 | $-1638.69 | -7.3% | $-638.69 | -3.6 | done | losing for real |
| always_up | 2257 | 47.2 | 49.8 | $-2181.48 | -9.7% | $-1181.48 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3546 | 47.6 | 49.2 | $-2759.03 |
| ETH | 3919 | 47.9 | 48.6 | $-2773.38 |
| SOL | 4093 | 47.8 | 48.7 | $-3059.41 |
| XRP | 4135 | 48.5 | 48.6 | $-2280.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
