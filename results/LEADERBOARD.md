# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1110 windows, 30704 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3097 | 51.2 | 50.4 | $-789.24 | -2.5% | $210.76 | -1.4 | done | can't tell from luck |
| value_ev10 | 1430 | 37.8 | 39.1 | $-960.15 | -6.7% | $39.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2606 | 49.7 | 49.4 | $-1088.51 | -4.2% | $-88.51 | -2.1 | done | losing for real |
| value_ev5 | 2168 | 39.8 | 41.0 | $-1355.13 | -6.3% | $-355.13 | -2.5 | done | losing for real |
| trend_filter | 1818 | 49.2 | 50.4 | $-1372.21 | -7.5% | $-372.21 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2606 | 50.3 | 51.1 | $-1686.36 | -6.5% | $-686.36 | -3.4 | done | losing for real |
| coinflip | 4432 | 50.5 | 50.2 | $-1692.26 | -3.8% | $-692.26 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3097 | 48.8 | 50.2 | $-2117.63 | -6.8% | $-1117.63 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4432 | 50.7 | 51.4 | $-2382.26 | -5.4% | $-1382.26 | -3.7 | done | losing for real |
| always_up | 4432 | 47.5 | 49.3 | $-3596.88 | -8.1% | $-2596.88 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7030 | 48.4 | 49.0 | $-3520.85 |
| ETH | 7605 | 48.1 | 48.4 | $-4634.77 |
| SOL | 7993 | 48.0 | 48.4 | $-4524.40 |
| XRP | 8076 | 48.2 | 48.2 | $-4751.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
