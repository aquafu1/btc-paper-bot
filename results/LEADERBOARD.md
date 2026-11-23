# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1148 windows, 31734 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 613 | 34.6 | 35.2 | $-387.85 | -6.3% | $612.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1495 | 38.1 | 39.2 | $-932.36 | -6.2% | $67.64 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3185 | 50.9 | 50.4 | $-970.59 | -3.0% | $29.41 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2678 | 49.6 | 49.5 | $-1196.98 | -4.5% | $-196.98 | -2.3 | done | losing for real |
| value_ev5 | 2256 | 40.1 | 41.1 | $-1293.45 | -5.7% | $-293.45 | -2.3 | done | losing for real |
| trend_filter | 1883 | 48.9 | 50.5 | $-1532.30 | -8.1% | $-532.30 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2678 | 50.4 | 51.0 | $-1631.51 | -6.1% | $-631.51 | -3.2 | done | losing for real |
| coinflip | 4587 | 50.3 | 50.2 | $-1893.01 | -4.1% | $-893.01 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3185 | 49.1 | 50.2 | $-1971.48 | -6.2% | $-971.48 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4587 | 50.2 | 51.4 | $-2864.99 | -6.2% | $-1864.99 | -4.4 | done | losing for real |
| always_up | 4587 | 47.9 | 49.4 | $-3341.35 | -7.3% | $-2341.35 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7267 | 48.2 | 49.0 | $-3837.16 |
| ETH | 7863 | 48.1 | 48.4 | $-4629.45 |
| SOL | 8265 | 48.1 | 48.4 | $-4600.46 |
| XRP | 8339 | 48.1 | 48.2 | $-4948.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
