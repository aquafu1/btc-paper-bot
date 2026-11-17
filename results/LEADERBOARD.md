# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 618 windows, 17082 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1444 | 51.2 | 49.6 | $-155.69 | -1.1% | $844.31 | -0.4 | done | can't tell from luck |
| value_ev20 | 328 | 34.1 | 35.3 | $-254.70 | -7.8% | $745.30 | -1.1 | done | can't tell from luck |
| trend_filter | 991 | 50.5 | 50.9 | $-501.42 | -5.1% | $498.58 | -1.6 | done | can't tell from luck |
| value_ev10 | 793 | 38.1 | 39.4 | $-597.33 | -7.5% | $402.67 | -1.7 | done | can't tell from luck |
| value_ev5 | 1196 | 40.2 | 41.3 | $-790.34 | -6.6% | $209.66 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1747 | 50.6 | 51.0 | $-868.10 | -5.0% | $131.90 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1747 | 49.4 | 50.0 | $-888.14 | -5.1% | $111.86 | -2.1 | done | losing for real |
| coinflip | 2464 | 50.0 | 50.5 | $-1196.95 | -4.9% | $-196.95 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1444 | 48.8 | 51.4 | $-1385.08 | -9.6% | $-385.08 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2464 | 50.4 | 51.7 | $-1498.68 | -6.1% | $-498.68 | -3.1 | done | losing for real |
| always_up | 2464 | 47.2 | 49.7 | $-2234.00 | -9.1% | $-1234.00 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3880 | 48.1 | 49.2 | $-2483.54 |
| ETH | 4274 | 48.0 | 48.6 | $-2762.26 |
| SOL | 4436 | 47.9 | 48.8 | $-2931.95 |
| XRP | 4492 | 48.6 | 48.6 | $-2192.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
