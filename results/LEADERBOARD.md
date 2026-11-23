# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1201 windows, 33155 settled trades, 89 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 647 | 34.6 | 35.3 | $-418.79 | -6.5% | $581.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1583 | 38.7 | 39.2 | $-800.46 | -5.1% | $199.54 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3322 | 50.8 | 50.3 | $-1099.26 | -3.3% | $-99.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 2394 | 40.4 | 41.1 | $-1239.26 | -5.2% | $-239.26 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2776 | 49.5 | 49.4 | $-1290.51 | -4.6% | $-290.51 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2776 | 50.5 | 51.1 | $-1655.99 | -6.0% | $-655.99 | -3.2 | done | losing for real |
| trend_filter | 1956 | 48.6 | 50.5 | $-1705.09 | -8.7% | $-705.09 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3322 | 49.2 | 50.2 | $-2043.76 | -6.2% | $-1043.76 | -3.6 | done | losing for real |
| coinflip | 4793 | 50.1 | 50.1 | $-2127.53 | -4.4% | $-1127.53 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4793 | 50.2 | 51.4 | $-2983.81 | -6.2% | $-1983.81 | -4.4 | done | losing for real |
| always_up | 4793 | 47.9 | 49.3 | $-3488.22 | -7.3% | $-2488.22 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7619 | 48.1 | 48.9 | $-4310.31 |
| ETH | 8226 | 48.1 | 48.4 | $-4958.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
