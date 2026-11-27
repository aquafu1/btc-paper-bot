# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1565 windows, 38299 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 796 | 34.3 | 35.3 | $-599.84 | -7.5% | $400.16 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3791 | 50.9 | 50.0 | $-1010.89 | -2.7% | $-10.89 | -1.6 | done | can't tell from luck |
| value_ev10 | 1892 | 38.4 | 39.1 | $-1030.54 | -5.4% | $-30.54 | -1.9 | done | can't tell from luck |
| value_ev5 | 2842 | 40.4 | 41.0 | $-1439.92 | -5.1% | $-439.92 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3182 | 51.0 | 50.9 | $-1504.64 | -4.7% | $-504.64 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3182 | 49.0 | 49.2 | $-1677.95 | -5.3% | $-677.95 | -3.0 | done | losing for real |
| trend_filter | 2260 | 48.6 | 50.3 | $-1961.52 | -8.7% | $-961.52 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3791 | 49.1 | 50.2 | $-2328.60 | -6.1% | $-1328.60 | -3.8 | done | losing for real |
| coinflip | 5521 | 50.0 | 49.9 | $-2386.94 | -4.3% | $-1386.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5521 | 50.2 | 51.3 | $-3429.67 | -6.2% | $-2429.67 | -4.7 | done | losing for real |
| always_up | 5521 | 48.2 | 49.2 | $-3526.06 | -6.4% | $-2526.06 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10101 | 48.0 | 48.6 | $-5714.36 |
| ETH | 10888 | 48.0 | 47.8 | $-5597.98 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
