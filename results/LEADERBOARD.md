# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 520 windows, 14334 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1222 | 51.2 | 49.8 | $-182.73 | -1.5% | $817.27 | -0.5 | done | can't tell from luck |
| value_ev20 | 268 | 34.3 | 35.5 | $-194.82 | -7.3% | $805.18 | -0.9 | done | can't tell from luck |
| value_ev10 | 669 | 38.0 | 39.7 | $-526.88 | -7.9% | $473.12 | -1.7 | done | can't tell from luck |
| trend_filter | 840 | 49.4 | 50.7 | $-577.53 | -6.9% | $422.47 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1452 | 49.7 | 49.6 | $-577.89 | -4.0% | $422.11 | -1.5 | done | can't tell from luck |
| value_ev5 | 993 | 39.9 | 41.5 | $-741.77 | -7.5% | $258.23 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 1452 | 50.3 | 51.6 | $-979.76 | -6.7% | $20.24 | -2.6 | done | losing for real |
| coinflip | 2072 | 50.0 | 50.7 | $-1100.90 | -5.3% | $-100.90 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1222 | 48.8 | 51.4 | $-1147.24 | -9.4% | $-147.24 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2072 | 49.4 | 51.6 | $-1665.44 | -8.0% | $-665.44 | -3.8 | done | losing for real |
| always_up | 2072 | 46.6 | 50.1 | $-2308.59 | -11.1% | $-1308.59 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3240 | 47.3 | 49.2 | $-2677.61 |
| ETH | 3579 | 48.0 | 48.7 | $-2390.38 |
| SOL | 3738 | 47.6 | 49.0 | $-2759.53 |
| XRP | 3777 | 48.4 | 48.8 | $-2176.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
