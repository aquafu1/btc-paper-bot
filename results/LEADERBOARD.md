# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 1:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1079 windows, 29852 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 559 | 34.5 | 35.1 | $-325.88 | -5.8% | $674.12 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3020 | 51.3 | 50.5 | $-767.87 | -2.5% | $232.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1379 | 37.7 | 39.2 | $-954.46 | -6.9% | $45.54 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2536 | 49.7 | 49.6 | $-1136.36 | -4.5% | $-136.36 | -2.3 | done | losing for real |
| trend_filter | 1776 | 49.5 | 50.6 | $-1243.32 | -7.0% | $-243.32 | -3.0 | done | losing for real |
| value_ev5 | 2096 | 39.7 | 41.1 | $-1340.54 | -6.4% | $-340.54 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2536 | 50.3 | 51.1 | $-1615.87 | -6.4% | $-615.87 | -3.3 | done | losing for real |
| coinflip | 4310 | 50.5 | 50.3 | $-1663.14 | -3.9% | $-663.14 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4310 | 51.1 | 51.5 | $-2009.32 | -4.7% | $-1009.32 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3020 | 48.7 | 50.3 | $-2149.31 | -7.1% | $-1149.31 | -4.0 | done | losing for real |
| always_up | 4310 | 47.3 | 49.4 | $-3770.25 | -8.7% | $-2770.25 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6815 | 48.4 | 49.0 | $-3388.87 |
| ETH | 7389 | 48.2 | 48.5 | $-4476.20 |
| SOL | 7789 | 48.1 | 48.5 | $-4449.49 |
| XRP | 7859 | 48.2 | 48.3 | $-4661.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
