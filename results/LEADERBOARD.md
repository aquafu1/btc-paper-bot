# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1153 windows, 31867 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 614 | 34.5 | 35.2 | $-397.85 | -6.5% | $602.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1503 | 38.3 | 39.2 | $-861.63 | -5.7% | $138.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3199 | 50.8 | 50.4 | $-1027.24 | -3.2% | $-27.24 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2686 | 49.7 | 49.5 | $-1177.95 | -4.4% | $-177.95 | -2.3 | done | losing for real |
| value_ev5 | 2271 | 40.2 | 41.1 | $-1239.73 | -5.5% | $-239.73 | -2.2 | done | losing for real |
| trend_filter | 1888 | 49.0 | 50.5 | $-1518.54 | -8.0% | $-518.54 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2686 | 50.3 | 51.0 | $-1670.43 | -6.2% | $-670.43 | -3.3 | done | losing for real |
| coinflip | 4607 | 50.2 | 50.2 | $-1911.39 | -4.1% | $-911.39 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3199 | 49.2 | 50.2 | $-1948.27 | -6.1% | $-948.27 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4607 | 50.1 | 51.4 | $-2914.43 | -6.3% | $-1914.43 | -4.4 | done | losing for real |
| always_up | 4607 | 47.8 | 49.3 | $-3467.02 | -7.5% | $-2467.02 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7304 | 48.2 | 49.0 | $-3808.09 |
| ETH | 7899 | 48.1 | 48.4 | $-4673.79 |
| SOL | 8286 | 48.0 | 48.4 | $-4608.51 |
| XRP | 8378 | 48.1 | 48.2 | $-5044.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
