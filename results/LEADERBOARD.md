# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1609 windows, 38879 settled trades, 386 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 821 | 34.2 | 35.2 | $-645.00 | -7.9% | $355.00 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3837 | 50.8 | 50.0 | $-1013.42 | -2.6% | $-13.42 | -1.6 | done | can't tell from luck |
| value_ev10 | 1942 | 38.4 | 39.0 | $-1075.80 | -5.5% | $-75.80 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3211 | 51.0 | 50.9 | $-1475.93 | -4.6% | $-475.93 | -2.7 | done | losing for real |
| value_ev5 | 2907 | 40.4 | 41.0 | $-1513.27 | -5.2% | $-513.27 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3211 | 49.0 | 49.2 | $-1743.64 | -5.4% | $-743.64 | -3.1 | done | losing for real |
| trend_filter | 2283 | 48.5 | 50.4 | $-2033.23 | -8.9% | $-1033.23 | -4.4 | done | losing for real |
| coinflip | 5610 | 50.1 | 49.9 | $-2327.58 | -4.1% | $-1327.58 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3837 | 49.2 | 50.2 | $-2358.51 | -6.1% | $-1358.51 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5610 | 50.1 | 51.3 | $-3502.17 | -6.2% | $-2502.17 | -4.8 | done | losing for real |
| always_up | 5610 | 48.2 | 49.1 | $-3609.18 | -6.4% | $-2609.18 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10365 | 47.9 | 48.6 | $-5869.88 |
| ETH | 11204 | 48.0 | 47.7 | $-5843.61 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
