# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1509 windows, 37546 settled trades, 399 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 763 | 34.5 | 35.4 | $-561.57 | -7.4% | $438.43 | -1.6 | done | can't tell from luck |
| value_ev10 | 1833 | 38.6 | 39.2 | $-946.32 | -5.2% | $53.68 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3735 | 50.9 | 50.1 | $-970.91 | -2.6% | $29.09 | -1.6 | done | can't tell from luck |
| value_ev5 | 2764 | 40.6 | 41.1 | $-1344.19 | -4.9% | $-344.19 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3134 | 51.1 | 51.0 | $-1404.29 | -4.5% | $-404.29 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3134 | 48.9 | 49.2 | $-1747.92 | -5.6% | $-747.92 | -3.1 | done | losing for real |
| trend_filter | 2224 | 48.5 | 50.3 | $-1939.92 | -8.7% | $-939.92 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3735 | 49.1 | 50.2 | $-2300.43 | -6.2% | $-1300.43 | -3.8 | done | losing for real |
| coinflip | 5408 | 50.0 | 50.0 | $-2380.40 | -4.4% | $-1380.40 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5408 | 50.1 | 51.3 | $-3353.26 | -6.2% | $-2353.26 | -4.7 | done | losing for real |
| always_up | 5408 | 48.0 | 49.2 | $-3610.25 | -6.7% | $-2610.25 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9747 | 48.0 | 48.7 | $-5422.15 |
| ETH | 10489 | 48.0 | 47.9 | $-5553.09 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
