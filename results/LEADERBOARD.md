# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1235 windows, 33681 settled trades, 435 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 660 | 34.4 | 35.3 | $-474.16 | -7.2% | $525.84 | -1.4 | done | can't tell from luck |
| value_ev10 | 1611 | 38.7 | 39.2 | $-770.67 | -4.8% | $229.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3378 | 50.8 | 50.3 | $-1059.63 | -3.1% | $-59.63 | -1.8 | done | can't tell from luck |
| value_ev5 | 2435 | 40.5 | 41.1 | $-1227.46 | -5.0% | $-227.46 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2824 | 49.5 | 49.4 | $-1282.40 | -4.5% | $-282.40 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2824 | 50.5 | 51.1 | $-1661.52 | -5.9% | $-661.52 | -3.2 | done | losing for real |
| trend_filter | 1991 | 48.7 | 50.4 | $-1682.77 | -8.5% | $-682.77 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3378 | 49.2 | 50.2 | $-2100.44 | -6.2% | $-1100.44 | -3.7 | done | losing for real |
| coinflip | 4860 | 50.0 | 50.1 | $-2202.35 | -4.5% | $-1202.35 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4860 | 50.2 | 51.4 | $-2973.94 | -6.1% | $-1973.94 | -4.4 | done | losing for real |
| always_up | 4860 | 47.8 | 49.3 | $-3575.83 | -7.4% | $-2575.83 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7871 | 48.0 | 48.9 | $-4509.50 |
| ETH | 8500 | 48.1 | 48.3 | $-4917.45 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
