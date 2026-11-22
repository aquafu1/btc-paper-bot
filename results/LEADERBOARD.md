# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1135 windows, 31368 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 602 | 34.6 | 35.2 | $-373.62 | -6.2% | $626.38 | -1.2 | done | can't tell from luck |
| value_ev10 | 1470 | 38.2 | 39.2 | $-900.10 | -6.1% | $99.90 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3157 | 51.0 | 50.5 | $-935.65 | -3.0% | $64.35 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2648 | 49.7 | 49.4 | $-1119.54 | -4.2% | $-119.54 | -2.2 | done | losing for real |
| value_ev5 | 2224 | 40.1 | 41.1 | $-1292.03 | -5.8% | $-292.03 | -2.3 | done | losing for real |
| trend_filter | 1860 | 49.1 | 50.4 | $-1419.83 | -7.6% | $-419.83 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2648 | 50.3 | 51.1 | $-1680.20 | -6.3% | $-680.20 | -3.4 | done | losing for real |
| coinflip | 4534 | 50.3 | 50.2 | $-1861.36 | -4.1% | $-861.36 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3157 | 49.0 | 50.2 | $-1992.18 | -6.3% | $-992.18 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4534 | 50.3 | 51.4 | $-2752.98 | -6.1% | $-1752.98 | -4.2 | done | losing for real |
| always_up | 4534 | 47.8 | 49.3 | $-3363.54 | -7.4% | $-2363.54 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7184 | 48.4 | 49.0 | $-3633.34 |
| ETH | 7771 | 48.2 | 48.4 | $-4548.76 |
| SOL | 8166 | 48.0 | 48.4 | $-4639.14 |
| XRP | 8247 | 48.1 | 48.2 | $-4869.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
