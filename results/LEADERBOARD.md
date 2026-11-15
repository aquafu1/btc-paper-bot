# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 384 windows, 10464 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 10:00 PM | too few trades (196/200) |
| value_ev10 | 505 | 39.8 | 40.5 | $-237.29 | -4.7% | $762.71 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 877 | 50.3 | 49.8 | $-309.07 | -3.5% | $690.93 | -1.1 | done | can't tell from luck |
| value_ev5 | 745 | 41.5 | 42.1 | $-366.06 | -4.9% | $633.94 | -1.2 | done | can't tell from luck |
| trend_filter | 584 | 48.8 | 50.6 | $-461.51 | -7.9% | $538.49 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1048 | 48.8 | 49.7 | $-587.41 | -5.6% | $412.59 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1048 | 51.2 | 52.1 | $-591.05 | -5.6% | $408.95 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 877 | 49.7 | 52.0 | $-733.13 | -8.4% | $266.87 | -2.6 | done | losing for real |
| coinflip | 1528 | 49.9 | 50.8 | $-821.70 | -5.4% | $178.30 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1528 | 49.3 | 51.5 | $-1191.69 | -7.8% | $-191.69 | -3.2 | done | losing for real |
| always_up | 1528 | 45.5 | 50.7 | $-2120.88 | -13.9% | $-1120.88 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2359 | 47.4 | 49.4 | $-1873.21 |
| ETH | 2629 | 47.5 | 48.9 | $-1928.13 |
| SOL | 2711 | 47.8 | 49.4 | $-2103.57 |
| XRP | 2765 | 48.5 | 49.1 | $-1541.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
