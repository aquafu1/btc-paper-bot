# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1611 windows, 38901 settled trades, 378 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 822 | 34.2 | 35.2 | $-655.00 | -8.0% | $345.00 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3840 | 50.9 | 50.0 | $-1007.14 | -2.6% | $-7.14 | -1.6 | done | can't tell from luck |
| value_ev10 | 1944 | 38.4 | 39.0 | $-1078.33 | -5.5% | $-78.33 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3212 | 51.1 | 50.9 | $-1470.36 | -4.6% | $-470.36 | -2.7 | done | losing for real |
| value_ev5 | 2909 | 40.4 | 41.0 | $-1515.80 | -5.2% | $-515.80 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3212 | 48.9 | 49.2 | $-1753.64 | -5.5% | $-753.64 | -3.1 | done | losing for real |
| trend_filter | 2283 | 48.5 | 50.4 | $-2033.23 | -8.9% | $-1033.23 | -4.4 | done | losing for real |
| coinflip | 5613 | 50.1 | 49.9 | $-2340.12 | -4.2% | $-1340.12 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3840 | 49.1 | 50.2 | $-2371.04 | -6.2% | $-1371.04 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5613 | 50.2 | 51.3 | $-3499.13 | -6.2% | $-2499.13 | -4.8 | done | losing for real |
| always_up | 5613 | 48.2 | 49.1 | $-3602.90 | -6.4% | $-2602.90 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10370 | 47.9 | 48.6 | $-5878.46 |
| ETH | 11221 | 48.0 | 47.7 | $-5863.99 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
