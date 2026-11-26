# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1477 windows, 37152 settled trades, 361 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 753 | 34.3 | 35.4 | $-587.37 | -7.8% | $412.63 | -1.6 | done | can't tell from luck |
| value_ev10 | 1810 | 38.5 | 39.2 | $-954.15 | -5.3% | $45.85 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3702 | 50.9 | 50.1 | $-988.14 | -2.7% | $11.86 | -1.6 | done | can't tell from luck |
| value_ev5 | 2729 | 40.4 | 41.1 | $-1427.88 | -5.2% | $-427.88 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3107 | 49.1 | 49.2 | $-1560.88 | -5.0% | $-560.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3107 | 50.9 | 51.0 | $-1569.23 | -5.1% | $-569.23 | -2.9 | done | losing for real |
| trend_filter | 2207 | 48.6 | 50.3 | $-1918.00 | -8.7% | $-918.00 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3702 | 49.1 | 50.2 | $-2300.56 | -6.2% | $-1300.56 | -3.8 | done | losing for real |
| coinflip | 5345 | 50.0 | 50.0 | $-2376.06 | -4.4% | $-1376.06 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5345 | 50.0 | 51.3 | $-3456.41 | -6.5% | $-2456.41 | -4.9 | done | losing for real |
| always_up | 5345 | 48.0 | 49.2 | $-3564.99 | -6.7% | $-2564.99 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9569 | 48.0 | 48.7 | $-5245.41 |
| ETH | 10273 | 47.9 | 48.0 | $-5874.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
