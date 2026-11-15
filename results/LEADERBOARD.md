# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 465 windows, 12760 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 236 | 34.7 | 35.9 | $-162.48 | -6.9% | $837.52 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1079 | 50.8 | 49.9 | $-292.42 | -2.7% | $707.58 | -0.9 | done | can't tell from luck |
| value_ev10 | 604 | 38.9 | 40.1 | $-393.68 | -6.5% | $606.32 | -1.3 | done | can't tell from luck |
| trend_filter | 737 | 49.8 | 50.7 | $-422.44 | -5.7% | $577.56 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1288 | 49.8 | 50.0 | $-500.02 | -3.9% | $499.98 | -1.4 | done | can't tell from luck |
| value_ev5 | 893 | 40.9 | 41.8 | $-537.06 | -6.0% | $462.94 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1288 | 50.2 | 51.6 | $-910.61 | -7.1% | $89.39 | -2.7 | done | losing for real |
| coinflip | 1852 | 50.0 | 50.8 | $-997.95 | -5.4% | $2.05 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1079 | 49.2 | 51.8 | $-1009.35 | -9.4% | $-9.35 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1852 | 49.9 | 51.6 | $-1253.52 | -6.8% | $-253.52 | -3.0 | done | losing for real |
| always_up | 1852 | 46.3 | 50.4 | $-2236.37 | -12.1% | $-1236.37 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2888 | 47.6 | 49.2 | $-2218.14 |
| ETH | 3201 | 48.1 | 48.8 | $-2054.28 |
| SOL | 3324 | 47.7 | 49.3 | $-2574.13 |
| XRP | 3347 | 48.5 | 49.2 | $-1869.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
