# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 906 windows, 24993 settled trades, 80 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1143 | 38.4 | 39.1 | $-563.08 | -4.9% | $436.92 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2114 | 49.9 | 49.8 | $-944.86 | -4.5% | $55.14 | -2.1 | done | losing for real |
| value_ev5 | 1730 | 40.1 | 41.0 | $-947.46 | -5.5% | $52.54 | -1.9 | done | can't tell from luck |
| trend_filter | 1482 | 49.9 | 51.0 | $-1006.14 | -6.8% | $-6.14 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2549 | 50.4 | 50.5 | $-1068.40 | -4.2% | $-68.40 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2549 | 49.6 | 50.4 | $-1327.49 | -5.2% | $-327.49 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2114 | 50.1 | 50.9 | $-1349.95 | -6.4% | $-349.95 | -3.0 | done | losing for real |
| coinflip | 3616 | 50.2 | 50.3 | $-1605.95 | -4.4% | $-605.95 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3616 | 51.2 | 51.7 | $-1651.31 | -4.6% | $-651.31 | -2.8 | done | losing for real |
| always_up | 3616 | 46.8 | 49.7 | $-3590.97 | -9.9% | $-2590.97 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5696 | 48.3 | 49.1 | $-3097.21 |
| ETH | 6213 | 48.2 | 48.5 | $-3718.73 |
| SOL | 6522 | 48.2 | 48.6 | $-3704.85 |
| XRP | 6562 | 48.3 | 48.5 | $-3636.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
