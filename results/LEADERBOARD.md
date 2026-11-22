# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1056 windows, 29237 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2962 | 51.3 | 50.4 | $-729.81 | -2.5% | $270.19 | -1.3 | done | can't tell from luck |
| value_ev10 | 1353 | 37.6 | 39.2 | $-960.78 | -7.1% | $39.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2487 | 49.7 | 49.6 | $-1182.80 | -4.8% | $-182.80 | -2.4 | done | losing for real |
| trend_filter | 1741 | 49.3 | 50.7 | $-1368.58 | -7.9% | $-368.58 | -3.4 | done | losing for real |
| value_ev5 | 2053 | 39.6 | 41.0 | $-1385.37 | -6.7% | $-385.37 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2487 | 50.3 | 51.0 | $-1553.66 | -6.2% | $-553.66 | -3.2 | done | losing for real |
| coinflip | 4216 | 50.5 | 50.3 | $-1717.92 | -4.1% | $-717.92 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2962 | 48.7 | 50.3 | $-2118.32 | -7.2% | $-1118.32 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4216 | 50.7 | 51.5 | $-2285.30 | -5.4% | $-1285.30 | -3.6 | done | losing for real |
| always_up | 4216 | 47.3 | 49.4 | $-3631.46 | -8.6% | $-2631.46 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6663 | 48.3 | 49.0 | $-3540.22 |
| ETH | 7233 | 48.1 | 48.5 | $-4588.44 |
| SOL | 7633 | 48.1 | 48.5 | $-4430.05 |
| XRP | 7708 | 48.2 | 48.3 | $-4683.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
