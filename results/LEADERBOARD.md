# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1202 windows, 33165 settled trades, 120 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 647 | 34.6 | 35.3 | $-418.79 | -6.5% | $581.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1584 | 38.6 | 39.2 | $-810.46 | -5.1% | $189.54 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3323 | 50.8 | 50.3 | $-1109.26 | -3.3% | $-109.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 2395 | 40.4 | 41.1 | $-1249.26 | -5.2% | $-249.26 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2777 | 49.5 | 49.4 | $-1278.95 | -4.6% | $-278.95 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2777 | 50.5 | 51.1 | $-1665.99 | -6.0% | $-665.99 | -3.2 | done | losing for real |
| trend_filter | 1957 | 48.6 | 50.5 | $-1693.53 | -8.7% | $-693.53 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3323 | 49.2 | 50.2 | $-2032.20 | -6.1% | $-1032.20 | -3.6 | done | losing for real |
| coinflip | 4794 | 50.1 | 50.1 | $-2137.53 | -4.5% | $-1137.53 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4794 | 50.2 | 51.4 | $-2972.25 | -6.2% | $-1972.25 | -4.4 | done | losing for real |
| always_up | 4794 | 47.9 | 49.3 | $-3476.66 | -7.3% | $-2476.66 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7619 | 48.1 | 48.9 | $-4310.31 |
| ETH | 8236 | 48.1 | 48.4 | $-4950.33 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
