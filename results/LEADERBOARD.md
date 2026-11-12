# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 121 windows, 3087 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 229 | 61.1 | 53.0 | $+297.92 | +13.0% | $1297.92 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 293 | 56.7 | 51.8 | $+206.59 | +7.1% | $1206.59 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 476 | 52.1 | 50.9 | $-85.03 | -1.8% | $914.97 | -0.4 | done | can't tell from luck |
| value_ev10 | 162 | 38.3 | 40.4 | $-158.93 | -9.8% | $841.07 | -1.1 | Thu 7:15 AM | too few trades (162/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 1:00 AM | too few trades (61/200) |
| coinflip | 476 | 50.2 | 51.1 | $-288.83 | -6.1% | $711.17 | -1.4 | done | can't tell from luck |
| trend_filter | 163 | 41.1 | 49.0 | $-314.23 | -19.3% | $685.77 | -2.4 | Thu 7:00 AM | too few trades (163/200) |
| value_ev5 | 229 | 37.6 | 42.0 | $-330.08 | -14.4% | $669.92 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 293 | 43.3 | 50.2 | $-481.09 | -16.4% | $518.91 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 229 | 38.9 | 49.2 | $-527.49 | -23.0% | $472.51 | -3.5 | done | losing for real |
| always_up | 476 | 45.6 | 50.2 | $-634.28 | -13.3% | $365.72 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 663 | 45.2 | 49.6 | $-709.74 |
| ETH | 756 | 45.1 | 48.8 | $-828.28 |
| SOL | 823 | 48.2 | 48.6 | $-603.42 |
| XRP | 845 | 49.6 | 48.9 | $-356.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
